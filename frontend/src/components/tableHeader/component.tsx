import React from 'react';
import {SearchField } from "../searchField/component";
import { Filter } from "../filter/component";
import styles from './component.module.css'
import { Button } from '@gravity-ui/uikit';

export const TableHeader = () => {
    return (
        <div className={styles.main}>
            <Filter />
            <SearchField />
            <Button view='action' size='l' >{'+ Создать курс'}</Button>
        </div>
      );
}