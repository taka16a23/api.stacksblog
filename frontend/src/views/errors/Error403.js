import React, { Component } from "react";
import { withTranslation } from 'react-i18next';

class Error403 extends Component {

  render() {
    return (
      <div class="error-box" style={{background: "none"}}>
        <div class="error-body text-center">
          <h1 class="error-title ">
            403
          </h1>
          <h3 class="text-uppercase error-subtitle">
            {this.props.t("PAGE FORBIDDEN !")}
          </h3>
          <p class="text-muted mt-4 mb-4">
            {this.props.t("YOU SEEM TO BE TRYING TO FIND HIS WAY HOME")}
          </p>
          <a href="/" class="btn btn-danger btn-rounded waves-effect waves-light mb-5">
            {this.props.t("Back to home")}
          </a>
        </div>
      </div>
    );
  };
}
export default withTranslation()(Error403);
