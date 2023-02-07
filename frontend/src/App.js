// import './App.css';

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'

import Header from './components/Header'
import Carousel from './components/Carousel';
import Footer from './components/Footer';
import Instructions from './components/Instructions';


function App() {


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
      </Routes>
      <Footer />
    </div>
    </Router>
  )
}

export default App;
