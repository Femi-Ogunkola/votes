import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'

export default function LogInButton() {
    return (
        <div className={styles.button}>
            <button>
                <p>Log In</p>
            </button>
        </div>
    )
}