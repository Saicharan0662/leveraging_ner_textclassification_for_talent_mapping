import React from 'react'
import { useNavigate } from 'react-router'

const Landing = () => {
    const navigate = useNavigate()

    return (
        <div>
            <h1>Welcome to *GOOD NAME*</h1>
            <button onClick={() => navigate('/home')}>Get Started</button>
        </div>
    )
}

export default Landing  