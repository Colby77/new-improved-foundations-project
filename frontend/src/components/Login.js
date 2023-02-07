const Login = () => {
  return (
    <div>
        <h3>This is the Login Page</h3>
        <form>
            <input type='text' placeholder='Username'></input>
            <input type='password' placeholder='Password'></input>
            <button type='submit'>Login</button>
        </form>
        <h3>No Account? Create an account to save and share characters</h3>
        <form>
            <input type='text' placeholder='Username'></input>
            <input type='password' placeholder='Password'></input>
            <button type='submit'>Register</button>
        </form>
    </div>
  )
}

export default Login