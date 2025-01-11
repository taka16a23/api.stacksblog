import React, { Component } from "react";
import PostCard from 'components/PostCard';
import { ServiceFactory } from 'services';
import queryString from 'query-string';
import ReactPaginate from 'react-paginate';
import { withTranslation } from 'react-i18next';
import Spinner from "views/spinner/Spinner";


class PostList extends Component {

  constructor(props) {
    super(props);
    this.models = [];
    this.state = {
      modelLength: this.models.length,
      isLoaded: false,
      start: 0,
      perPage: 5
    }
  }

  pageChange(data) {
    let pageNumber = data['selected'];
    this.setState({
      start: pageNumber * this.state.perPage
    });
    window.scrollTo({top: 0, behavior: 'smooth'});
  }

  componentDidMount() {
    var oParams = new URLSearchParams();
    let oGetParams = queryString.parse(window.location.search);
    if(oGetParams.category__name !== undefined && Array.isArray(oGetParams.category__name) === true) {
      oGetParams.category__name.forEach(strCategoryName => {
        oParams.append('category__name', strCategoryName);
      })
    }
    if(oGetParams.category__name !== undefined && Array.isArray(oGetParams.category__name) !== true) {
      oParams.append('category__name', oGetParams.category__name);
    }
    oParams.append('ordering', "-created_at");
    var blogService = ServiceFactory.createBlogService();
    blogService.listPosts(oParams).then(arrModels => {
      this.models = arrModels;
      this.setState({
        modelLength: this.models.length,
        isLoaded: true,
      });
    }).catch(err => {
      alert(err);
    });
  }

  render() {
    if(this.state.isLoaded !== true) {
      return (
        <Spinner/>
      )
    }
    if(this.state.isLoaded === true && this.models.length <= 0) {
      return (
        <div>
          <div className="text-center text-white">
            <h3 className="font-bold">
              {this.props.t("POST NOT FOUND !")}
            </h3>
            <p className="mt-4 mb-4 font-bold">
              {this.props.t("YOU SEEM TO BE TRYING TO FIND HIS WAY HOME")}
            </p>
            <a href="/" className="bg-pink-700 hover:bg-pink-800 focus:ring-4 focus:ring-pink-300 font-medium rounded-md text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-pink-600 dark:hover:bg-pink-700 focus:outline-none dark:focus:ring-pink-800">
              <span className="font-bold">{this.props.t("Back to home")}</span>
            </a>
          </div>
        </div>
      )
    }

    return (
      <>
        <div>
          {this.models.slice(
            this.state.start, this.state.start + this.state.perPage).map(
              (oPostModel) => <PostCard post={oPostModel} key={oPostModel.slug}/>
            )
          }
        </div>
        <div role="navigation">
          <ReactPaginate
            pageCount={Math.ceil(this.models.length / this.state.perPage)}
            marginPagesDisplayed={3}
            pageRangeDisplayed={5}
            onPageChange={this.pageChange.bind(this)}
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
