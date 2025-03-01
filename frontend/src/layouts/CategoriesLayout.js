import React, { Component, lazy } from 'react';

import { NavLink, Routes, Route } from "react-router-dom";

import PostList from 'components/PostList';
import PostDetail from 'views/blog/PostDetail';

import { ServiceFactory } from 'services';


const Error404 = lazy(() => new Promise((resolve) => {
  setTimeout(() => resolve(import("views/errors/Error404")), 0);
}));


class CategoriesLayout extends Component {

  constructor(props) {
    super(props)
    this.models = [];
    this.state = {
      modelLength: this.models.length,
      categoryName: null,
    }
  }

  componentDidMount() {
    var blogService = ServiceFactory.createBlogService();
    var oParams = new URLSearchParams();
    oParams.append('ordering', "name");
    blogService.listCategories(oParams).then(models => {
      this.models = models;
      this.setState({modelLength: this.models.length});
    }).catch(err => {
      alert(err);
    });
  }

  handleOnClick(categoryName) {
    this.setState({
      categoryName: categoryName,
    });
  }


  render() {
    return (
        <div className="container mx-auto px-10 mb-8">
          <div className='grid grid-cols-1 lg:grid-cols-12 gap-12'>
            <div className="lg:col-span-8 col-span-1">
              <Routes>
                <Route path="/post/:id" element={<PostDetail/>}/>
                <Route path="/*" element={<PostList categoryName={this.state.categoryName}/>}/>
                <Route path='*' element={<Error404/>}/>
              </Routes>
            </div>
            <div className="lg:col-span-4 col-span-1">
              <div className="lg:sticky relative top-8">
                <div className='bg-white shadow-lg rounded-lg p-8 mb-4 pb-8'>
                  <h2 className='text-xl mb-4 font-semibold text-neutral-500 border-b pb-4'>
                    カテゴリー
                  </h2>
                  {this.models.map((category) => (
                    <NavLink to={"/"} className="cursor-pointer text-neutral-500 no-underline hover:underline hover:text-blue-700" key={category.category_id} onClick={() => {this.handleOnClick(category.name)}}>
                      <span className='block pb-1 mb-1'>
                        {category.name}
                      </span>
                    </NavLink>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>
    )
  }
}

export default CategoriesLayout;
