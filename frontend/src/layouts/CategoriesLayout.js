import React, { Component, lazy } from 'react';
import { Routes, Route } from "react-router-dom";
import PostList from 'components/PostList'
import PostDetail from 'views/blog/PostDetail';

const Categories = lazy(() => import("components/Categories"));

const Error404 = lazy(() => new Promise((resolve) => {
  setTimeout(() => resolve(import("views/errors/Error404")), 0);
}));


class CategoriesLayout extends Component {

  render() {
    return (
        <div className="container mx-auto px-10 mb-8">
          <div className='grid grid-cols-1 lg:grid-cols-12 gap-12'>
            <div className="lg:col-span-8 col-span-1">
              <Routes>
                <Route path="/" element={<PostList/>}/>
                <Route path="/post/:slug" element={<PostDetail/>}/>
                <Route path='*' element={<Error404/>}/>
              </Routes>
            </div>
            <div className="lg:col-span-4 col-span-1">
              <div className="lg:sticky relative top-8">
                <Categories/>
              </div>
            </div>
          </div>
        </div>
    )
  }
}

export default CategoriesLayout;
