import React, { Component } from "react";
import { withTranslation } from 'react-i18next';

class Error404 extends Component {

  render() {
    return (
      <div className="error-box" style={{background: "none"}}>
        <div className="text-center text-white font-extrabold">
          <h1>
            404
          </h1>
          <h3 className="text-uppercase error-subtitle text-white font-bold">
            {this.props.t("PAGE NOT FOUND !")}
          </h3>
          <p className="mt-4 mb-4 text-white font-bold">
            {this.props.t("YOU SEEM TO BE TRYING TO FIND HIS WAY HOME")}
          </p>
          <a href="/" className="text-white bg-pink-700 hover:bg-pink-800 focus:ring-4 focus:ring-pink-300 font-medium rounded-md text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-pink-600 dark:hover:bg-pink-700 focus:outline-none dark:focus:ring-pink-800">
            {this.props.t("Back to home")}
          </a>
        </div>
      </div>
    );
  };
}
export default withTranslation()(Error404);
