import {Menu, Checkbox, Button, ArrowToggle} from '@gravity-ui/uikit';
import { useState } from 'react';
import coursesAll from '../../../data/courses.json'
import teachers from '../../../data/teachers.json'

import { useReactiveVar } from '@apollo/client';
import { filtersTableVar } from '../../../pages/mainPage/mainPage';
import { coursesVar } from '../../../pages/mainPage/mainPage';

export const ListFilters = () => {
    const [isOpen, setIsOpen] = useState(false)
    const filters = useReactiveVar(filtersTableVar)

    const changeStateFilters = (id:number) => {
        const newFilters = filters.slice(0)
        newFilters[id].value = !filters[id].value
        filtersTableVar(newFilters)
    }

    const checkGoodTeacher = (teacherName: string) => {
        const teacherCurrent = teachers.filter((item) => item.teacher === teacherName)
        return teacherCurrent[0].assessment > 4.7
    }

    const eventApplyFilters = () => {
        const checked = [filtersTableVar()[0].value, filtersTableVar()[1].value, filtersTableVar()[2].value, filtersTableVar()[3].value]
        const newListCourses = coursesAll.filter((item) => 
         (!checked[0] || !item.passed) && (!checked[1] || item.extern) && (!checked[2] || item.lightness > 4.7) && (!checked[3]) || checkGoodTeacher(item.teacher))
        coursesVar(newListCourses)
        setIsOpen(false)  
        const newAfterApply = filters.slice(0)
        const cntFilters = newAfterApply.length
        for (let i = 0; i < cntFilters; i++) {
            newAfterApply[i].value = false
        }
        filtersTableVar(newAfterApply)
    }

    return (
        <div>
            {!isOpen && <Button onClick={()=>setIsOpen(true)}><ArrowToggle direction="right" /></Button>}
            {isOpen &&
            <div> 
                <Button onClick={()=>setIsOpen(false)}><ArrowToggle direction="bottom" /></Button>
                <Menu size="m">
                {filters.map((item, id) => (
                    <Menu.Item><Checkbox content={item.name} checked={item.value} onChange={() => changeStateFilters(id)}/></Menu.Item>
                ))}
                </Menu>
                <Button onClick={()=>eventApplyFilters()}>Применить Фильтры</Button>
            </div>}
        </div>
    )
}