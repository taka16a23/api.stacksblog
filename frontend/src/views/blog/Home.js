import React, { Component } from "react";
import Categories from "components/Categories";
import PostList from 'components/PostList'


class HomeComponent extends Component {

  render() {
    return (
        <div className="container mx-auto px-10 mb-8">
          <div className='grid grid-cols-1 lg:grid-cols-12 gap-12'>
            <div className="lg:col-span-8 col-span-1">
              <PostList/>
            </div>
            <div className="lg:col-span-4 col-span-1">
              <div className="lg:sticky relative top-8">
                <Categories/>
              </div>
            </div>
          </div>
        </div>
    );
  };
}

export default HomeComponent;
