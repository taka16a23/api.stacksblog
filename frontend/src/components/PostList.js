import React, { Component } from "react";

import ReactPaginate from 'react-paginate';
import { withTranslation } from 'react-i18next';

import PostCard from 'components/PostCard';
import PostNotFound from 'components/PostNotFound';
import { ServiceFactory } from 'services';


class PostList extends Component {

  constructor(props) {
    super(props);
    this.list_post_ids = [];
    this.state = {
      listPostIdsLength: this.list_post_ids.length,
      isLoaded: false,
      start: 0,
      perPage: 5,
      categoryName: props.CategoryName,
    }
  }

  getPosts(categoryName) {
    var oParams = new URLSearchParams();
    if(categoryName !== null) {
      console.log(categoryName)
      oParams.append('category__name', categoryName);
    }
    oParams.append('ordering', "-publish_date");
    var blogService = ServiceFactory.createBlogService();
    blogService.listPostIds(oParams).then(ids => {
      this.list_post_ids = ids;
      this.setState({
        listPostIdsLength: this.list_post_ids.length,
        isLoaded: true,
        categoryName: categoryName,
      });
    }).catch(err => {
      alert(err);
    });
  }

  componentDidMount() {
    this.getPosts(this.props.categoryName);
  }

  shouldComponentUpdate(nextProps: Props, nextState: State) {
    if(this.state.categoryName !== nextProps.categoryName) {
      this.getPosts(nextProps.categoryName);
    }
    return true;
  }

  handlePageChange(data) {
    let pageNumber = data['selected'];
    console.log(pageNumber);
    this.setState({
      start: pageNumber * this.state.perPage
    });
    window.scrollTo({top: 0, behavior: 'smooth'});
  }

  render() {
    if(this.state.isLoaded === true && this.list_post_ids.length <= 0) {
      return (
        <PostNotFound/>
      )
    }

    return (
      <>
        <div>
          {this.list_post_ids.slice(
            this.state.start, this.state.start + this.state.perPage).map(
              (id) => <PostCard post_id={id} key={id}/>
            )
          }
        </div>
        <div role="navigation">
          <ReactPaginate
            pageCount={Math.ceil(this.list_post_ids.length / this.state.perPage)}
            marginPagesDisplayed={3}
            pageRangeDisplayed={5}
            onPageChange={this.handlePageChange.bind(this)}
            containerClassName='pagination list-style-none flex justify-center'
            pageClassName='page-item ml-2'
            pageLinkClassName='font-bold relative block rounded px-3 py-1.5 text-md text-white transition-all duration-300 hover:bg-neutral-100 dark:text-white dark:hover:bg-neutral-700 hover:text-blue-700'
            activeClassName='active bg-pink-600 rounded text-blue-700'
            previousLabel={this.props.t("Previous")}
            nextLabel={this.props.t("Next")}
            previousClassName='relative block rounded px-3 py-1.5 font-bold text-md text-white transition-all duration-300 hover:bg-neutral-100 dark:text-white dark:hover:bg-neutral-700 hover:text-blue-700'
            nextClassName='relative block rounded ml-2 px-3 py-1.5 font-bold text-md text-white transition-all duration-300 hover:bg-neutral-100 dark:text-white dark:hover:bg-neutral-700 hover:text-blue-700'
            previousLinkClassName=''
            nextLinkClassName=''
            disabledClassName='disabled'
            breakLabel='...'
            breakClassName='font-bold text-white'
            breakLinkClassName='page-link'
          />
        </div>
      </>
    );
  };
}

export default withTranslation()(PostList);
