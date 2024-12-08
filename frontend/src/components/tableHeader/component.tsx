import {SearchField } from "../searchField/component";
import { Button } from "../button/component";
import { Filter } from "../filter/component";
import styles from './component.module.css'

export const TableHeader = () => {
    return (
        <div className={styles.main}>
            <Filter />
            <SearchField />
            <Button label={'+ Создать курс'}/>
        </div>
      );
}