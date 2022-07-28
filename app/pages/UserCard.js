import Link from 'next/link';
import styles from '../styles/Card.module.css'


const UserCard = ({ user }) => {
    return (
        <div className={styles.card}>
            {/* <img src={user.avatar} alt="Avatar" style={{ width: '100%' }} /> */}
            <div className={styles.container}>
                <div>{user.title}</div><br />
                <div>{user.description}</div>
                {/* <p>{user.options}</p> */}
            </div>
        </div>
    );
}
export default UserCard;
