import {Avatar as GravityAvatar} from '@gravity-ui/uikit';
import styles from './component.module.css'

import img from '../../data/img/ava.jpeg'

type HeaderProps = {
    headingName: string;
};

export const Header: React.FC<HeaderProps> = ({headingName}) => {
    return (
        <div className={styles.header}>
            <div className={styles.heading}>{headingName}</div>
            <GravityAvatar imgUrl={img} />
        </div>
    )
}
    