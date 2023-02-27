import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import axios from 'axios'

import Header from './components/Header'
import Carousel from './components/Carousel';
import Footer from './components/Footer';
import Instructions from './components/Instructions';
import Login from './components/Login'


function App() {

  const registerUser = async (user) => {
    // console.log(user)
    await axios.post('/users/', user)
    .then((res) => {
      console.log(res.data)
    })
    .catch(err => console.log(err))
    
  }

  return (
    <Router>
    <div>
    <Header />
      <Routes>
        <Route
          path='/'
          element={
            <Carousel />
          } />
        <Route
          path='/create-char'
          element={
            <Instructions />
          } />
        <Route
          path='/account'
          element={
            <Login onRegister={registerUser}/>
          } />
      </Routes>
      <Footer />
    </div>
    </Router>
  )
}

export default App;
