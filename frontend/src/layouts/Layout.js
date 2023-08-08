import React, { Component, lazy } from 'react';
import { Routes, Route } from "react-router-dom";
import Header from 'components/Header';
import Home from 'views/blog/Home';


const PostDetail = lazy(() => new Promise((resolve) => {
  setTimeout(() => resolve(import("views/blog/PostDetail")), 0);
}));

const Error403 = lazy(() => new Promise((resolve) => {
  setTimeout(() => resolve(import("views/errors/Error403")), 0);
}));
const Error404 = lazy(() => new Promise((resolve) => {
  setTimeout(() => resolve(import("views/errors/Error404")), 0);
}));


class Layout extends Component {

  render() {
    return (
      <>
        <Header/>
        <Routes>
          <Route exact={true} path='/errors/403' element={<Error403/>}/>
          <Route path="/" element={<Home/>}/>
          <Route path="/post/:slug" element={<PostDetail/>}/>
          <Route path='*' element={<Error404/>}/>
        </Routes>
      </>
    )
  }
}

export default Layout;
