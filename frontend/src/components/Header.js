import React, { Component } from "react";
import { NavLink } from 'react-router-dom'

class Header extends Component {

  render() {
    return (
        <div className='container mx-auto px-10 mb-8'>
            <div className="border-b w-full inline-block border-blue-400 py-8">
                <div className='md:float-left block'>
                    <NavLink to="/">
                        <span className='cursor-pointer font-bold text-4xl text-white'>
                            {process.env.REACT_APP_NAME}
                        </span>
                    </NavLink>
                </div>
                <div className='hidden md:float-left md:contents'>
                  <NavLink className="" to="https://taka16a23.com">
                    <span className='md:float-right hover:text-pink-600 mt-2 align-middle text-white ml-4 font-semibold cursor-pointer'>
                      My Portfolio
                    </span>
                  </NavLink>
                </div>
            </div>
        </div>
    );
  };
}

export default Header;
