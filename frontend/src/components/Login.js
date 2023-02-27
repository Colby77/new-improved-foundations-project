import { useState } from 'react'


const Login = ({ onRegister }) => {

  const [username, setUsername] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')

  const onSubmit = (e) => {
    e.preventDefault()
    onRegister({ username, email, password })

    setUsername('')
    setEmail('')
    setPassword('')
  }


  return (
    <div>
        <h3>This is the Login Page</h3>
        <form>
            <input type='email' placeholder='Email'></input>
            <input type='password' placeholder='Password'></input>
            <button type='submit'>Login</button>
        </form>
        <h3>No Account? Create an account to save and share characters</h3>
        <form onSubmit={onSubmit}>
            <input type='text' placeholder='Username' 
            value={username} onChange={(e) => setUsername(e.target.value)} />
            <input type='email' placeholder='Email' 
            value={email} onChange={(e) => setEmail(e.target.value)} />
            <input type='password' placeholder='Password' 
            value={password} onChange={(e) => setPassword(e.target.value)} />
            <button type='submit'>Register</button>
        </form>
    </div>
  )
}

export default Login