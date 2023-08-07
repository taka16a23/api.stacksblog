import React, { Component } from "react";
import Categories from "components/Categories";
import queryString from 'query-string';
import PostList from 'components/PostList'


class HomeComponent extends Component {

  constructor(props) {
    super(props)
    this.state = {
      categories: [],
    }
  }

  componentDidMount() {
    let oGetParams = queryString.parse(window.location.search);
    let arrCategories = [];
    if(oGetParams.category !== undefined && Array.isArray(oGetParams.category) === true) {
      oGetParams.category.forEach(strCategoryId => {
        let iCategoryID = parseInt(strCategoryId);
        if(isNaN(iCategoryID) !== true) {
          arrCategories.push(iCategoryID);
        }
      })
    }
    if(oGetParams.category !== undefined && Array.isArray(oGetParams.category) !== true) {
      let iCategoryID = parseInt(oGetParams.category);
        if(isNaN(iCategoryID) !== true) {
          arrCategories.push(iCategoryID);
        }
    }
    this.setState({
      categories: arrCategories
    });
  }

  render() {
    return (
        <div className="container mx-auto px-10 mb-8">
          <div className='grid grid-cols-1 lg:grid-cols-12 gap-12'>
            <PostList categories={this.state.categories}/>
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
