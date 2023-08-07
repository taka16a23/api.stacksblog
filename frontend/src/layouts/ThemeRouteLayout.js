import React, { Component } from "react";
import { Route, Redirect } from "react-router-dom";
import { ServiceFactory } from 'services';


export default class ThemeRouteLayout extends Component {

  constructor(props) {
    super(props)
    this.service = ServiceFactory.createPageService();
  }

  render() {
    let {
      routes
    } = this.props;
    if(routes === undefined) {
      routes = [];
    }
    return (
      routes.map((prop, key) => {
        if(prop.menu_type === 1) {
          return null;
        }
        if(prop.redirect) {
          return <Redirect from={prop.path} to={prop.pathTo} key={key}/>;
        }
        if(prop.menu_type === 3) {
          return <ThemeRouteLayout props={this.props.props} routes={prop.child} key={key}/>;
        }
        if(this.service.getComponent(prop.path) === undefined) {
          return null;
        }
        return <Route path={prop.path} component={this.service.getComponent(prop.path)} key={key}/>;
      })
    );
  };
};
