import React, { Component } from "react";
import PostCard from 'components/PostCard';
import { ServiceFactory } from 'services';
import queryString from 'query-string';


class PostList extends Component {

  constructor(props) {
    super(props);
    this.models = [];
    this.state = {
      modelLength: this.models.length,
    }
  }

  componentDidMount() {
    var oParams = new URLSearchParams();
    let oGetParams = queryString.parse(window.location.search);
    if(oGetParams.category !== undefined && Array.isArray(oGetParams.category) === true) {
      oGetParams.category.forEach(strCategoryId => {
        let iCategoryID = parseInt(strCategoryId);
        if(isNaN(iCategoryID) !== true) {
          oParams.append('category', iCategoryID);
        }
      })
    }
    if(oGetParams.category !== undefined && Array.isArray(oGetParams.category) !== true) {
      let iCategoryID = parseInt(oGetParams.category);
        if(isNaN(iCategoryID) !== true) {
          oParams.append('category', iCategoryID);
        }
    }
    var blogService = ServiceFactory.createBlogService();
    blogService.listPosts(oParams).then(arrModels => {
      console.log("DEBUG-1-PostList.js")
      this.models = arrModels;
      this.setState({modelLength: this.models.length});
    }).catch(err => {
      alert(err);
    });
  }

  render() {
    return (
      <div className="lg:col-span-8 col-span-1">
        {this.models.map((oPostModel) => <PostCard post={oPostModel} key={oPostModel.slug}/>)}
      </div>
    );
  };
}

export default PostList;
