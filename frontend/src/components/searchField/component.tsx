import {useState} from 'react';

import {TextInput as GravityTextInput, Button} from '@gravity-ui/uikit';

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
      <div>
        <GravityTextInput placeholder={'Search...'} name={searchValue} onChange={(it) => searchVar(it.target.value)} className = {styles.main}/>
        <Button onClick={() => eventSearchCourse()}>Найти</Button>
      </div>
      );
}