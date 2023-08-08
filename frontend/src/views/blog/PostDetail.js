import React, { Component } from "react";
import withRouter from "helpers/WithRouter";
import moment from 'moment';
import Categories from 'components/Categories';
import { ServiceFactory } from 'services';
import { PostModel } from 'models';


class PostDatailComponent extends Component {

  constructor(props) {
    super(props)
    this.state = {
      model: new PostModel(),
    }
  }

  componentDidMount() {
    var blogService = ServiceFactory.createBlogService();
    blogService.getPost(this.props.params.slug).then(models => {
      if (models.length <= 0) {
        return;
      }
      this.setState({model: models[0]});
    }).catch(err => {
      alert(err);
    });
  }

  render() {
    return (
        <div className="container mx-auto px-10 mb-8">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-12">
            <div className="col-span-1 lg:col-span-8">
              <div className='bg-white shadow-lg rounded-lg lg:p-8 pb-12 mb-8'>
                <div className='relative overflow-hidden shadow-md mb-6'>
                  <img
                    src={this.state.model.image}
                    alt={this.state.model.title}
                    className="object-top h-full w-full rounded-t-lg"
                  />
                </div>
                <div className='px-4 lg:px-0'>
                  <div className='flex items-center mb-8 w-full'>
                    <div className='font-medium text-gray-700'>
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 inline mr-2 text-pink-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                      </svg>
                      <span>
                        {moment(this.state.model.created_at).format('DD, MMM, YYYY')}
                      </span>
                    </div>
                  </div>
                  <h1 className='mb-8 text-3xl font-semibold'>{this.state.model.title}</h1>
                  <div dangerouslySetInnerHTML={{__html: this.state.model.content}} />
                </div>
              </div>

              {/* <Author author={post.author} /> */}
              {/* <AdjacentPosts slug={post.slug} createdAt={post.createdAt} /> */}
              {/* <CommentsForm slug={post.slug} /> */}
              {/* <Comments slug={post.slug} /> */}
            </div>
            <div className="col-span-1 lg:col-span-4">
              <div className="relative lg:sticky top-8">
                  {/*<PostWidget slug={post.slug} categories={post.categories.map((category) => category.slug)} />*/}
                  <Categories />
              </div>
            </div>
          </div>
        </div>
    )
  }
}
export default withRouter(PostDatailComponent);
