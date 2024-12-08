import {Avatar as GravityAvatar} from '@gravity-ui/uikit';
import styles from './component.module.css'

type HeaderProps = {
    imgUrl: string;
    headingName: string;
};

export const Header: React.FC<HeaderProps> = ({headingName, imgUrl}) => {
    return (
        <div className={styles.header}>
            <div className={styles.heading}>{headingName}</div>
            <GravityAvatar imgUrl={imgUrl} />
        </div>
    )
}
    