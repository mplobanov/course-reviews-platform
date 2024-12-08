import {useState} from 'react';

import {TextInput as GravityTextInput} from '@gravity-ui/uikit';
import { Button } from '../button/component';

import styles from './component.module.css'
import coursesAll from '../../data/courses.json'

import { searchVar } from '../../pages/mainPage/mainPage';
import { coursesVar } from '../../pages/mainPage/mainPage';

import { useReactiveVar } from '@apollo/client';

export const SearchField = () => {
    const searchValue = useReactiveVar(searchVar)

    const eventSearchCourse = () => {
      const findCourses = coursesAll.filter((item) => (item.nameCourse.includes(searchValue) || item.teacher.includes(searchValue)))
      coursesVar(findCourses)
    }

    return (
      <div className = {styles.main}>
        <GravityTextInput placeholder={'Search...'} name={searchValue} onChange={(it) => searchVar(it.target.value)} className={styles.searchField} size="l"/>
        <Button label={'Найти'} onClick={() => eventSearchCourse()}/>
      </div>
      );
}