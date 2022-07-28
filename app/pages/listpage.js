import UserCard from './UserCard';
import styles from '../styles/Users.module.css'
export const getStaticProps = async () => {
    const res = await fetch('http://0.0.0.0:8000/poll/');
    const { data } = await res.json();
    return {
        props: { users: data }
    }
}
const Users = ({ users }) => {
    return (
        <div className={`container ${styles.userlist}`} >
            {users.map(user => (
                <UserCard key={user.id} user={user} />
            ))}
        </div>
    );
}
export default Users;
