import React, { Component, lazy } from 'react';
import { Routes, Route } from "react-router-dom";

import Header from 'components/Header';
import CategoriesLayout from 'layouts/CategoriesLayout';

const Error403 = lazy(() => new Promise((resolve) => {
  setTimeout(() => resolve(import("views/errors/Error403")), 0);
}));


class Layout extends Component {

  render() {
    return (
      <>
        <Header/>
        <Routes>
          <Route exact={true} path='/errors/403' element={<Error403/>}/>
          <Route path="*" element={<CategoriesLayout/>}/>
        </Routes>
      </>
    )
  }
}

export default Layout;
