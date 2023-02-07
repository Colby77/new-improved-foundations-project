import { Link } from 'react-router-dom'


const Header = () => {
  return (
    <header>
        <img alt='wizard-logo'></img>
        <nav>
            <ul>
                <li><Link to='/'>Home</Link></li>
                <li><Link to='/create-char'>Create Character</Link></li>
                <li><Link>Shop</Link></li>
                <li><Link>About</Link></li>
            </ul>
        </nav>
        <div>
            <img alt='cart'></img>
            <h4><Link to='/account'>Account</Link></h4>
        </div>
    </header>
  )
}

export default Header