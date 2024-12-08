import React from 'react';
import { TableHeader } from '../../components/tableHeader/component';
import { Table } from '../../components/tableCourses/component';

import courses from '../../data/courses.json';
import filters from '../../data/filterTable.json';

import { makeVar } from '@apollo/client';

import styles from './mainPage.module.css';
import { PageHead } from '../../components/page-head/component';

export const coursesVar = makeVar(courses);
export const filtersTableVar = makeVar(filters);
export const searchVar = makeVar('');

export const MainPage = () => {
  return (
    <PageHead>
      <div className={styles.tableSpace}>
        <TableHeader />
        <Table />
      </div>
    </PageHead>
  );
};
