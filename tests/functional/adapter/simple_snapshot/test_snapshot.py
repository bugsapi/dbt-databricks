from typing import Optional

from dbt.tests import util
from dbt.tests.adapter.simple_snapshot.test_snapshot import BaseSimpleSnapshot
from dbt.tests.adapter.simple_snapshot.test_snapshot import BaseSnapshotCheck


class TestSnapshot(BaseSimpleSnapshot):
    def add_fact_column(self, column: Optional[str] = None, definition: Optional[str] = None):
        """
        Applies updates to a table in a dbt project

        Args:
            project: the dbt project that contains the table
            table: the name of the table without a schema
            column: the name of the new column
            definition: the definition of the new column, e.g. 'varchar(20) default null'
        """

        table_name = util.relation_from_name(self.project.adapter, "fact")
        sql = f"""
            alter table {table_name}
            add column {column} string
        """
        self.project.run_sql(sql)


class TestSnapshotCheck(BaseSnapshotCheck):
    pass
