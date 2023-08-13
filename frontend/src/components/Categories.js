import React, { Component } from "react";
import { ServiceFactory } from 'services';


class Categories extends Component {

  constructor(props) {
    super(props)
    this.models = [];
    this.state = {
      modelLength: this.models.length,
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

  render() {
    return (
      <div className='bg-white shadow-lg rounded-lg p-8 mb-4 pb-8'>
        <h2 className='text-xl mb-4 font-semibold text-neutral-500 border-b pb-4'>
          カテゴリー
        </h2>
        {this.models.map((category) => (
          <a key={category.category_id} href={"/?category__name=" + category.name} className="cursor-pointer text-neutral-500 no-underline hover:underline hover:text-blue-700">
            <span className='block pb-1 mb-1'>
              {category.name}
            </span>
          </a>
        ))}
      </div>
    );
  };
}

export default Categories;
