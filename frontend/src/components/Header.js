const Header = () => {
  return (
    <header>
        <img alt='wizard-logo'></img>
        <nav>
            <ul>
                <li><a href='/'>Home</a></li>
                <li><a href='/create-char'>Create Character</a></li>
                <li><a>Shop</a></li>
                <li><a>About</a></li>
            </ul>
        </nav>
        <div>
            <img alt='cart'></img>
            <h4>Account</h4>
        </div>
    </header>
  )
}

export default Header