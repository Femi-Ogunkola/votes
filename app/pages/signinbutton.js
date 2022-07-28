import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'

export default function SignInButton() {
    return (
        <div className={styles.button}>
            <button>
                <p>SIGN IN</p>
            </button>
        </div>
    )
}