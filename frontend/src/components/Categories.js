import React, { Component } from "react";

import { NavLink } from 'react-router-dom'

import { ServiceFactory } from 'services';


export default class Categories extends Component {

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
          <NavLink to={"/?category__name=" + category.name} className="cursor-pointer text-neutral-500 no-underline hover:underline hover:text-blue-700" key={category.category_id}>
            <span className='block pb-1 mb-1'>
              {category.name}
            </span>
          </NavLink>
        ))}
      </div>
    );
  };
}
