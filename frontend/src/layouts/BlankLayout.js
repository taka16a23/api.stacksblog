import React, { Component } from "react";
import { Route, Switch } from "react-router-dom";
import { ServiceFactory } from 'services';


class Blanklayout extends Component {
  constructor(props) {
    super(props)
    this.service = ServiceFactory.createPageService();
  }

  render() {
    return (
      <div>
        <Switch>
          <Route path={this.props.path} component={this.service.getComponent(this.props.path)} />
        </Switch>
      </div>
    );
  }
};
export default Blanklayout;
