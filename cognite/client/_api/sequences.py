import copy
import math
from typing import *

from cognite.client import utils
from cognite.client._api_client import APIClient
from cognite.client.data_classes import Sequence, SequenceData, SequenceFilter, SequenceList, SequenceUpdate
from cognite.client.utils._experimental_warning import experimental_api


@experimental_api(api_name="Sequences")
class SequencesAPI(APIClient):
    _RESOURCE_PATH = "/sequences"
    _LIST_CLASS = SequenceList

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = SequencesDataAPI(self, *args, **kwargs)

    def __call__(
        self,
        chunk_size: int = None,
        name: str = None,
        external_id_prefix: str = None,
        metadata: Dict[str, Any] = None,
        asset_ids: List[int] = None,
        root_asset_ids: List[int] = None,
        created_time: Dict[str, Any] = None,
        last_updated_time: Dict[str, Any] = None,
        limit: int = None,
    ) -> Generator[Union[Sequence, SequenceList], None, None]:
        """Iterate over sequences

        Fetches sequences as they are iterated over, so you keep a limited number of objects in memory.

        Args:
            chunk_size (int, optional): Number of sequences to return in each chunk. Defaults to yielding one event a time.
            name (str): Filter out sequences that do not have this *exact* name.
            external_id_prefix (str): Filter out sequences that do not have this string as the start of the externalId
            metadata (Dict[str, Any]): Filter out sequences that do not match these metadata fields and values (case-sensitive). Format is {"key1":"value1","key2":"value2"}.
            asset_ids (List[int]): Filter out sequences that are not linked to any of these assets.
            root_asset_ids (List[int]): Filter out sequences not linked to assets with one of these assets as the root asset.
            created_time (Dict[str, Any]): Filter out sequences with createdTime outside this range.
            last_updated_time (Dict[str, Any]): Filter out sequences with lastUpdatedTime outside this range.
            limit (int, optional): Max number of sequences to return. Defaults to return all items.

        Yields:
            Union[Sequence, SequenceList]: yields Sequence one by one if chunk is not specified, else SequenceList objects.
        """
        filter = SequenceFilter(
            name=name,
            metadata=metadata,
            external_id_prefix=external_id_prefix,
            asset_ids=asset_ids,
            root_asset_ids=root_asset_ids,
            created_time=created_time,
            last_updated_time=last_updated_time,
        ).dump(camel_case=True)
        return self._list_generator(method="GET", chunk_size=chunk_size, filter=filter, limit=limit)

    def __iter__(self) -> Generator[Sequence, None, None]:
        """Iterate over sequences

        Fetches sequences as they are iterated over, so you keep a limited number of metadata objects in memory.

        Yields:
            Sequence: yields Sequence one by one.
        """
        return self.__call__()

    def retrieve(self, id: Optional[int] = None, external_id: Optional[str] = None) -> Optional[Sequence]:
        """Retrieve a single sequence by id.

        Args:
            id (int, optional): ID
            external_id (str, optional): External ID

        Returns:
            Optional[Sequence]: Requested sequences or None if it does not exist.

        Examples:

            Get sequences by id::

                >>> from cognite.client.experimental import CogniteClient
                >>> c = CogniteClient()
                >>> res = c.sequences.retrieve(id=1)

            Get sequences by external id::

                >>> from cognite.client.experimental import CogniteClient
                >>> c = CogniteClient()
                >>> res = c.sequences.retrieve(external_id="1")
        """
        utils._auxiliary.assert_exactly_one_of_id_or_external_id(id, external_id)
        return self._retrieve_multiple(ids=id, external_ids=external_id, wrap_ids=True)

    def retrieve_multiple(
        self, ids: Optional[List[int]] = None, external_ids: Optional[List[str]] = None
    ) -> SequenceList:
        """Retrieve multiple sequences by id.

        Args:
            ids (List[int], optional): IDs
            external_ids (List[str], optional): External IDs

        Returns:
            SequenceList: The requested sequences.

        Examples:

            Get sequences by id::

                >>> from cognite.client.experimental import CogniteClient
                >>> c = CogniteClient()
                >>> res = c.sequences.retrieve_multiple(ids=[1, 2, 3])

            Get sequences by external id::

                >>> from cognite.client.experimental import CogniteClient
                >>> c = CogniteClient()
                >>> res = c.sequences.retrieve_multiple(external_ids=["abc", "def"])
        """
        utils._auxiliary.assert_type(ids, "id", [List], allow_none=True)
        utils._auxiliary.assert_type(external_ids, "external_id", [List], allow_none=True)
        return self._retrieve_multiple(ids=ids, external_ids=external_ids, wrap_ids=True)

    def list(
        self,
        name: str = None,
        external_id_prefix: str = None,
        metadata: Dict[str, Any] = None,
        asset_ids: List[int] = None,
        root_asset_ids: List[int] = None,
        created_time: Dict[str, Any] = None,
        last_updated_time: Dict[str, Any] = None,
        limit: Optional[int] = 25,
    ) -> SequenceList:
        """Iterate over sequences

        Fetches sequences as they are iterated over, so you keep a limited number of objects in memory.

        Args:
            name (str): Filter out sequences that do not have this *exact* name.
            external_id_prefix (str): Filter out sequences that do not have this string as the start of the externalId
            metadata (Dict[str, Any]): Filter out sequences that do not match these metadata fields and values (case-sensitive). Format is {"key1":"value1","key2":"value2"}.
            asset_ids (List[int]): Filter out sequences that are not linked to any of these assets.
            root_asset_ids (List[int]): Filter out sequences not linked to assets with one of these assets as the root asset.
            created_time (Dict[str, Any]): Filter out sequences with createdTime outside this range.
            last_updated_time (Dict[str, Any]): Filter out sequences with lastUpdatedTime outside this range.
            limit (int, optional): Max number of sequences to return. Defaults to 25. Set to -1, float("inf") or None
                to return all items.

        Returns:
            SequenceList: The requested sequences.

        Examples:

            List sequences::

                >>> from cognite.client.experimental import CogniteClient
                >>> c = CogniteClient()
                >>> res = c.sequences.list(limit=5)

            Iterate over sequences::

                >>> from cognite.client.experimental import CogniteClient
                >>> c = CogniteClient()
                >>> for seq in c.sequences:
                ...     seq # do something with the sequences

            Iterate over chunks of sequences to reduce memory load::

                >>> from cognite.client.experimental import CogniteClient
                >>> c = CogniteClient()
                >>> for seq_list in c.sequences(chunk_size=2500):
                ...     seq_list # do something with the sequences
        """
        filter = SequenceFilter(
            name=name,
            metadata=metadata,
            external_id_prefix=external_id_prefix,
            asset_ids=asset_ids,
            root_asset_ids=root_asset_ids,
            created_time=created_time,
            last_updated_time=last_updated_time,
        ).dump(camel_case=True)
        return self._list(method="POST", filter=filter, limit=limit)

    def create(self, sequence: Union[Sequence, List[Sequence]]) -> Union[Sequence, SequenceList]:
        """Create one or more sequences.

        Args:
            sequence (Union[Sequence, List[Sequence]]): Sequence or list of Sequence to create.

        Returns:
            Union[Sequence, SequenceList]: The created sequences.

        Examples:

            Create a new sequence::

                >>> from cognite.client.experimental import CogniteClient
                >>> from cognite.client.data_classes import Sequence
                >>> c = CogniteClient()
                >>> seq = c.sequences.create(Sequence(external_id="my_sequence", columns=[{'valueType':'STRING'},{'valueType':'DOUBLE'}]))

            Create a new sequence with the same column specifications as an existing sequence::

                >>> seq2 = c.sequences.create(Sequence(external_id="my_copied_sequence", columns=seq.columns))

        """
        utils._auxiliary.assert_type(sequence, "sequences", [List, Sequence])
        if isinstance(sequence, list):
            sequence = [self._clean_columns(seq) for seq in sequence]
        else:
            sequence = self._clean_columns(sequence)
        return self._create_multiple(items=sequence)

    def _clean_columns(self, sequence):
        sequence = copy.copy(sequence)
        sequence.columns = [
            {v: col[v] for v in ["externalId", "valueType", "metadata"] if v in col} for col in sequence.columns
        ]
        return sequence

    def delete(self, id: Union[int, List[int]] = None, external_id: Union[str, List[str]] = None) -> None:
        """Delete one or more sequences.

        Args:
            id (Union[int, List[int]): Id or list of ids
            external_id (Union[str, List[str]]): External ID or list of external ids

        Returns:
            None

        Examples:

            Delete sequences by id or external id::

                >>> from cognite.client.experimental import CogniteClient
                >>> c = CogniteClient()
                >>> c.sequences.delete(id=[1,2,3], external_id="3")
        """
        self._delete_multiple(wrap_ids=True, ids=id, external_ids=external_id)

    def update(
        self, item: Union[Sequence, SequenceUpdate, List[Union[Sequence, SequenceUpdate]]]
    ) -> Union[Sequence, SequenceList]:
        """Update one or more sequences.

        Args:
            item (Union[Sequence, SequenceUpdate, List[Union[Sequence, SequenceUpdate]]]): Sequences to update

        Returns:
            Union[Sequence, SequenceList]: Updated sequences.

        Examples:

            Update a sequences that you have fetched. This will perform a full update of the sequences::

                >>> from cognite.client.experimental import CogniteClient
                >>> c = CogniteClient()
                >>> res = c.sequences.retrieve(id=1)
                >>> res.description = "New description"
                >>> res = c.sequences.update(res)

            Perform a partial update on a sequences, updating the description and adding a new field to metadata::

                >>> from cognite.client.experimental import CogniteClient
                >>> from cognite.client.data_classes import SequenceUpdate
                >>> c = CogniteClient()
                >>> my_update = SequenceUpdate(id=1).description.set("New description").metadata.add({"key": "value"})
                >>> res = c.sequences.update(my_update)
        """
        return self._update_multiple(items=item)

    def search(
        self,
        name: str = None,
        description: str = None,
        query: str = None,
        filter: Union[SequenceFilter, Dict] = None,
        limit: int = None,
    ) -> SequenceList:
        """Search for sequences.

        Args:
            name (str, optional): Prefix and fuzzy search on name.
            description (str, optional): Prefix and fuzzy search on description.
            query (str, optional): Search on name and description using wildcard search on each of the words (separated
                by spaces). Retrieves results where at least one word must match. Example: 'some other'
            filter (Union[SequenceFilter, Dict], optional): Filter to apply. Performs exact match on these fields.
            limit (int, optional): Max number of results to return.

        Returns:
            SequenceList: List of requested sequences.

        Examples:

            Search for a sequences::

                >>> from cognite.client.experimental import CogniteClient
                >>> c = CogniteClient()
                >>> res = c.sequences.search(name="some name")
        """
        return self._search(
            search={"name": name, "description": description, "query": query}, filter=filter, limit=limit
        )


class SequencesDataAPI(APIClient):
    _DATA_PATH = "/sequences/data"

    def __init__(self, sequences_api, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._sequences_api = sequences_api
        self._SEQ_POST_LIMIT = 10000
        self._SEQ_RETRIEVE_LIMIT = 10000

    def insert(
        self,
        rows: Union[
            Dict[int, List[Union[int, float, str]]],
            List[Tuple[int, Union[int, float, str]]],
            List[Dict[str, Any]],
            SequenceData,
        ],
        column_ids: Optional[List[int]] = None,
        column_external_ids: Optional[List[str]] = None,
        id: int = None,
        external_id: str = None,
    ) -> None:
        """Insert rows into a sequence

        Args:
            column_ids (Optional[List[int]]): List of ids for the columns of the sequence.
                If 'None' is passed to both column_ids and columns_external_ids, all columns ids will be retrieved from metadata and used in that order.
            column_external_ids (Optional[List[str]]): List of external id for the columns of the sequence.
            rows (Union[ Dict[int, List[Union[int, float, str]]], List[Tuple[int,Union[int, float, str]]], List[Dict[str,Any]], SequenceData]):  The rows you wish to insert.
                Can either be a list of tuples, a list of {"rowNumber":... ,"values": ...} objects, a dictionary of rowNumber: data, or a SequenceData object. See examples below.
            id (int): Id of sequence to insert rows into.
            external_id (str): External id of sequence to insert rows into.

        Returns:
            None

        Examples:
            Your rows of data can be a list of tuples where the first element is the rownumber and the second element is the data to be inserted::

                >>> from cognite.client.experimental import CogniteClient
                >>> c = CogniteClient()
                >>> seq = c.sequences.create(Sequence(columns=[{"valueType": "STRING","valueType": "DOUBLE"}]))
                >>> data = [(1, ['pi',3.14]), (2, ['e',2.72]) ]
                >>> c.sequences.data.insert(column_ids=seq.column_ids, rows=data, id=1)

            They can also be provided as a list of API-style objects with a rowNumber and values field::

                >>> from cognite.client.experimental import CogniteClient
                >>> c = CogniteClient()
                >>> data = [{"rowNumber": 123, "values": ['str',3]}, {"rowNUmber": 456, "values": ["bar",42]} ]
                >>> c.sequences.data.insert(data, id=1) # implicit columns are retrieved from metadata

            Or they can be a given as a dictionary with row number as the key, and the value is the data to be inserted at that row::

                >>> from cognite.client.experimental import CogniteClient
                >>> c = CogniteClient()
                >>> data = {123 : ['str',3], 456 : ['bar',42] }
                >>> c.sequences.data.insert(column_external_ids=['stringColumn','intColumn'], rows=data, id=1)

            Finally, they can be a SequenceData object retrieved from another request. In this case column_external_ids from this object are used as well.

                >>> from cognite.client.experimental import CogniteClient
                >>> c = CogniteClient()
                >>> data = c.sequences.data.retrieve(id=2,start=0,end=10)
                >>> c.sequences.data.insert(rows=data, id=1)
        """
        utils._auxiliary.assert_exactly_one_of_id_or_external_id(id, external_id)
        if isinstance(rows, SequenceData):
            if column_ids is None and column_external_ids is None and (None not in rows.column_external_ids):
                column_external_ids = rows.column_external_ids
            rows = [{"rowNumber": k, "values": v} for k, v in rows.items()]

        if column_ids is None and column_external_ids is None:
            column_ids = self._sequences_api.retrieve(id=id, external_id=external_id).column_ids
        if isinstance(rows, dict):
            all_rows = [{"rowNumber": k, "values": v} for k, v in rows.items()]
        elif isinstance(rows, list) and len(rows) > 0 and isinstance(rows[0], dict):
            all_rows = rows
        elif isinstance(rows, list) and (len(rows) == 0 or isinstance(rows[0], tuple)):
            all_rows = [{"rowNumber": k, "values": v} for k, v in rows]
        else:
            raise ValueError("Invalid format for 'rows', expected a list of tuples, list of dict or dict")

        base_obj = self._process_ids(id, external_id, wrap_ids=True)[0]
        base_obj.update(self._process_columns(column_ids, column_external_ids))
        row_objs = [
            {"rows": all_rows[i : i + self._SEQ_POST_LIMIT]} for i in range(0, len(all_rows), self._SEQ_POST_LIMIT)
        ]
        tasks = [({**base_obj, **rows},) for rows in row_objs]
        summary = utils._concurrency.execute_tasks_concurrently(
            self._insert_data, tasks, max_workers=self._config.max_workers
        )
        summary.raise_compound_exception_if_failed_tasks()

    def insert_dataframe(
        self, dataframe, external_id_headers: bool = False, id: int = None, external_id: str = None
    ) -> None:
        """Insert a Pandas dataframe.

        The index of the dataframe must contain the row numbers. The names of the remaining columns specify the column ids or external ids (no mixed values allowed, and ids should be integers).
        The sequence and columns must already exist.

        Args:
            dataframe (pandas.DataFrame):  Pandas DataFrame object containing the sequence data.
            external_id_headers (bool): Headers are external ids
            id (int): Id of sequence to insert rows into.
            external_id (str): External id of sequence to insert rows into.

        Returns:
            None

        Examples:
            Multiply data in the sequence by 2::

                >>> from cognite.client.experimental import CogniteClient
                >>> c = CogniteClient()
                >>> df = c.sequences.data.retrieve_dataframe(id=123, start=0, end=None)
                >>> c.sequences.data.insert_dataframe(df*2, id=123, external_id_headers=True)
        """
        dataframe = dataframe.replace({math.nan: None})
        data = [(v[0], list(v[1:])) for v in dataframe.itertuples()]
        if external_id_headers:
            column_ids = None
            column_external_ids = list(dataframe.columns)
        else:
            column_ids = [int(h) for h in list(dataframe.columns)]
            column_external_ids = None
        self.insert(
            rows=data, column_ids=column_ids, column_external_ids=column_external_ids, id=id, external_id=external_id
        )

    def _insert_data(self, task):
        self._post(url_path=self._DATA_PATH, json={"items": [task]})

    def delete(self, rows: List[int], id: int = None, external_id: str = None) -> None:
        """Delete rows from a sequence

        Args:
            rows (List[int]): List of row numbers.
            id (int): Id of sequence to delete rows from.
            external_id (str): External id of sequence to delete rows from.

        Returns:
            None

        Examples:

                >>> from cognite.client.experimental import CogniteClient
                >>> c = CogniteClient()
                >>> c.sequences.data.delete(id=0, rows=[1,2,42])
        """
        utils._auxiliary.assert_exactly_one_of_id_or_external_id(id, external_id)
        post_obj = self._process_ids(id, external_id, wrap_ids=True)[0]
        post_obj["rows"] = rows

        self._post(url_path=self._DATA_PATH + "/delete", json={"items": [post_obj]})

    def delete_range(self, start: int, end: int, id: int = None, external_id: str = None) -> None:
        """Delete a range of rows from a sequence. Note this operation is potentially slow, as retrieves each row before deleting.

        Args:
            start (int): Row number to start from (inclusive).
            end (int): Upper limit on the row number (exclusive).
            id (int): Id of sequence to delete rows from.
            external_id (str): External id of sequence to delete rows from.

        Returns:
            None

        Examples:

                >>> from cognite.client.experimental import CogniteClient
                >>> c = CogniteClient()
                >>> c.sequences.data.delete_range(id=0, start=0, end=None)
        """
        deleter = lambda data: self.delete(rows=[r["rowNumber"] for r in data], external_id=external_id, id=id)
        utils._auxiliary.assert_exactly_one_of_id_or_external_id(id, external_id)
        sequence = self._sequences_api.retrieve(id=id, external_id=external_id)
        post_obj = self._process_ids(id, external_id, wrap_ids=True)[0]
        post_obj.update(self._process_columns(column_ids=[sequence.column_ids[0]], column_external_ids=None))
        post_obj.update({"inclusiveFrom": start, "exclusiveTo": end})
        self._fetch_data(post_obj, deleter)

    def retrieve(
        self,
        start: int,
        end: int,
        column_ids: Optional[List[int]] = None,
        column_external_ids: Optional[List[str]] = None,
        external_id: str = None,
        id: int = None,
    ) -> SequenceData:
        """Retrieve data from a sequence

        Args:
            start (int): Row number to start from (inclusive)
            end (int): Upper limit on the row number (exclusive)
            column_ids (Optional[List[int]]): List of ids for the columns of the sequence.
                If 'None' is passed to both column_ids and columns_external_ids, all columns will be retrieved.
            column_external_ids (Optional[List[str]]): List of external id for the columns of the sequence.
            id (int): Id of sequence
            external_id (str): External id of sequence

        Returns:
            List of sequence data

        Examples:

                >>> from cognite.client.experimental import CogniteClient
                >>> c = CogniteClient()
                >>> res = c.sequences.data.retrieve(id=0, start=0, end=None)
                >>> tuples = [(r,v) for r,v in res.items()] # You can use this iterator in for loops and list comprehensions,
                >>> single_value = res[23] # ... get the values at a single row number,
                >>> col = res.get_column(external_id='columnExtId') # ... get the array of values for a specific column,
                >>> df = res.to_pandas() # ... or convert the result to a dataframe
        """
        utils._auxiliary.assert_exactly_one_of_id_or_external_id(id, external_id)
        post_obj = self._process_ids(id, external_id, wrap_ids=True)[0]
        post_obj.update(self._process_columns(column_ids=column_ids, column_external_ids=column_external_ids))
        post_obj.update({"inclusiveFrom": start, "exclusiveTo": end})
        seqdata = []
        column_response = self._fetch_data(post_obj, lambda data: seqdata.extend(data))
        return SequenceData(id=id, external_id=external_id, rows=seqdata, columns=column_response)

    def retrieve_dataframe(
        self,
        start: int,
        end: int,
        column_ids: Optional[List[int]] = None,
        column_external_ids: Optional[List[str]] = None,
        external_id: str = None,
        id: int = None,
    ):
        """Retrieve data from a sequence as a pandas dataframe

        Args:
            start: (inclusive) row number to start from.
            end: (exclusive) upper limit on the row number.
            column_ids (Optional[List[int]]): List of ids for the columns of the sequence.
                If 'None' is passed to both column_ids and columns_external_ids, all columns will be retrieved.
            column_external_ids (Optional[List[str]]): List of external id for the columns of the sequence.
            id (int): Id of sequence
            external_id (str): External id of sequence.

        Returns:
             pandas.DataFrame

        Examples:

                >>> from cognite.client.experimental import CogniteClient
                >>> c = CogniteClient()
                >>> df = c.sequences.data.retrieve_dataframe(id=0, start=0, end=None)
        """
        return self.retrieve(start, end, column_ids, column_external_ids, external_id, id).to_pandas()

    def _fetch_data(self, task, callback):
        task["limit"] = self._SEQ_RETRIEVE_LIMIT
        columns = []
        cursor = None
        while True:
            task["cursor"] = cursor
            items = self._post(url_path=self._DATA_PATH + "/list", json={"items": [task]}).json()["items"]
            data = items[0]["rows"]
            columns = columns or items[0]["columns"]
            callback(data)
            cursor = items[0].get("cursor")
            if not cursor:
                break
        return columns

    def _process_columns(self, column_ids, column_external_ids):
        if column_ids is not None and column_external_ids is not None:
            raise ValueError("Expecting only exactly one of column_ids and column_external_ids to be set")
        if column_ids is None and column_external_ids is None:
            return {}  # retrieve API endpoint has implicit all columns retrieval
        if column_ids is not None:
            return {"columns": [{"id": col} for col in column_ids]}
        else:
            if any([c is None for c in column_external_ids]):
                raise ValueError("Some column external ids were None")
            return {"columns": [{"externalId": col} for col in column_external_ids]}