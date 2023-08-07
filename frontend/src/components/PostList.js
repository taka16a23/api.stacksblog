import React, { Component } from "react";
import PropTypes from 'prop-types';
import PostCard from 'components/PostCard';
import { ServiceFactory } from 'services';


class PostList extends Component {

  static propTypes = {
    categories: PropTypes.arrayOf(PropTypes.number),
  }

  static defaultProps = {
    categories: [],
  }

  constructor(props) {
    super(props);
    this.models = [];
    this.state = {
      modelLength: this.models.length,
    }
  }

  componentDidMount() {
    var oParams = new URLSearchParams();
    this.props.categories.forEach(iCategoryID => {
      oParams.append('category', iCategoryID);
    });
    var blogService = ServiceFactory.createBlogService();
    blogService.listPosts(oParams).then(arrModels => {
      this.models = arrModels
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
