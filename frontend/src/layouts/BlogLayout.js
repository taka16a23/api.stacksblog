import React, { Component, lazy } from 'react';
import Header from 'components/Header';
import { BrowserRouter, Routes, Route } from "react-router-dom";

const HomeComponent = lazy(() => new Promise((resolve) => {
  setTimeout(() => resolve(import("views/blog/Home")), 0);
}));

const PostDetailComponent = lazy(() => new Promise((resolve) => {
  setTimeout(() => resolve(import("views/blog/PostDetail")), 0);
}));

const Error403 = lazy(() => new Promise((resolve) => {
  setTimeout(() => resolve(import("views/errors/Error403")), 0);
}));
const Error404 = lazy(() => new Promise((resolve) => {
  setTimeout(() => resolve(import("views/errors/Error404")), 0);
}));


class BlogLayout extends Component {
  render() {
    return (
      <>
        <Header/>
        <Routes>
          <Route exact={true} path="/" element={<HomeComponent/>}/>
          <Route path="/post/:slug" element={<PostDetailComponent/>}/>
          <Route path='/errors/403' element={<Error403/>}/>
          <Route path='*' element={<Error404/>}/>
        </Routes>
      </>
    )
  }

}

export default BlogLayout;
