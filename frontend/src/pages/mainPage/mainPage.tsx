import { TableHeader } from '../../components/tableHeader/component';
import { Header } from '../../components/header/component';
import { Table } from '../../components/tableCourses/component';

import courses from '../../data/courses.json'
import filters from '../../data/filterTable.json'

import { makeVar } from '@apollo/client';

import styles from './mainPage.module.css';

export const coursesVar = makeVar(courses)
export const filtersTableVar = makeVar(filters)
export const searchVar = makeVar('')



export const MainPage = () => {
    return (
        <div>
            <Header headingName='Курсы 1С' imgUrl='../../../public/logo192.png'/>
                <div className={styles.tableSpace}>
                    <TableHeader />
                    <Table />
                </div>
        </div>
        
    )
}
