import React from 'react'
import Navigation from './header/navigation.js'
import Logo from './header/logo'
const Header = () => {

  return (
    <header id="header"> 
      <div className="container">
        <Logo title="Schoolify"/>
        <Navigation />
      </div> 
    </header>
  )
}

export default Header;
