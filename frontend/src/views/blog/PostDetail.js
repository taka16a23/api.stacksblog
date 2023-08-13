import React, { Component } from "react";
import withRouter from "helpers/WithRouter";
import moment from 'moment';
import Categories from 'components/Categories';
import { ServiceFactory } from 'services';
import { withTranslation } from 'react-i18next';
import Spinner from "views/spinner/Spinner";

import Prism from "prismjs";
import "prismjs/themes/prism-tomorrow.min.css";
import "prismjs/plugins/toolbar/prism-toolbar.min.css";
import "prismjs/plugins/toolbar/prism-toolbar.min";
import "prismjs/plugins/show-language/prism-show-language.min.js";
import "prismjs/plugins/line-numbers/prism-line-numbers.min.css";
import "prismjs/plugins/line-numbers/prism-line-numbers.min";
import "prismjs/plugins/copy-to-clipboard/prism-copy-to-clipboard.min";
import "prismjs/plugins/line-highlight/prism-line-highlight.min.css";
import "prismjs/plugins/line-highlight/prism-line-highlight.min.js";
import "prismjs/plugins/command-line/prism-command-line.min.css";
import "prismjs/plugins/command-line/prism-command-line.min.js";

import "prismjs/components/prism-python.min.js";
import "prismjs/components/prism-apacheconf.min.js";
import "prismjs/components/prism-bash.min.js";
import "prismjs/components/prism-json.min.js";
import "prismjs/components/prism-c";
import "prismjs/components/prism-autohotkey.min.js";
import "prismjs/components/prism-autoit.min.js";
import "prismjs/components/prism-awk.min.js";
import "prismjs/components/prism-bash.min.js";
import "prismjs/components/prism-basic.min.js";
import "prismjs/components/prism-batch.min.js";
import "prismjs/components/prism-cmake.min.js";
import "prismjs/components/prism-c.min.js";
import "prismjs/components/prism-cpp.min.js";
import "prismjs/components/prism-csharp.min.js";
import "prismjs/components/prism-css-extras.min.js";
import "prismjs/components/prism-css.min.js";
import "prismjs/components/prism-csv.min.js";
import "prismjs/components/prism-diff.min.js";
import "prismjs/components/prism-d.min.js";
import "prismjs/components/prism-dns-zone-file.min.js";
import "prismjs/components/prism-docker.min.js";
import "prismjs/components/prism-eiffel.min.js";
import "prismjs/components/prism-elixir.min.js";
import "prismjs/components/prism-excel-formula.min.js";
import "prismjs/components/prism-git.min.js";
import "prismjs/components/prism-go.min.js";
import "prismjs/components/prism-go-module.min.js";
import "prismjs/components/prism-haml.min.js";
import "prismjs/components/prism-haskell.min.js";
import "prismjs/components/prism-http.min.js";
import "prismjs/components/prism-icon.min.js";
import "prismjs/components/prism-ignore.min.js";
import "prismjs/components/prism-ini.min.js";
import "prismjs/components/prism-javadoclike.min.js";
import "prismjs/components/prism-java.min.js";
import "prismjs/components/prism-javascript.min.js";
import "prismjs/components/prism-js-extras.min.js";
import "prismjs/components/prism-json5.min.js";
import "prismjs/components/prism-json.min.js";
import "prismjs/components/prism-jsonp.min.js";
import "prismjs/components/prism-js-templates.min.js";
import "prismjs/components/prism-jsx.min.js";
import "prismjs/components/prism-kotlin.min.js";
import "prismjs/components/prism-lisp.min.js";
import "prismjs/components/prism-log.min.js";
import "prismjs/components/prism-makefile.min.js";
import "prismjs/components/prism-markdown.min.js";
import "prismjs/components/prism-markup.min.js";
import "prismjs/components/prism-markup-templating.min.js";
import "prismjs/components/prism-mongodb.min.js";
import "prismjs/components/prism-n4js.min.js";
import "prismjs/components/prism-nginx.min.js";
import "prismjs/components/prism-puppet.min.js";
import "prismjs/components/prism-python.min.js";
import "prismjs/components/prism-regex.min.js";
import "prismjs/components/prism-r.min.js";
import "prismjs/components/prism-ruby.min.js";
import "prismjs/components/prism-sass.min.js";
import "prismjs/components/prism-scheme.min.js";
import "prismjs/components/prism-scss.min.js";
import "prismjs/components/prism-shell-session.min.js";
import "prismjs/components/prism-smarty.min.js";
import "prismjs/components/prism-sql.min.js";
import "prismjs/components/prism-systemd.min.js";
import "prismjs/components/prism-textile.min.js";
import "prismjs/components/prism-tsx.min.js";
import "prismjs/components/prism-uri.min.js";
import "prismjs/components/prism-vim.min.js";
import "prismjs/components/prism-wiki.min.js";


class PostDatailComponent extends Component {

  constructor(props) {
    super(props)
    this.state = {
      isLoaded: false,
      model: null,
    }
  }

  componentDidMount() {
    var blogService = ServiceFactory.createBlogService();
    blogService.getPost(this.props.params.slug).then(models => {
      if (models.length <= 0) {
        this.setState({
          isLoaded: true,
        });
        return;
      }
      this.setState({
        isLoaded: true,
        model: models[0],
      });
      Prism.highlightAll();
    }).catch(err => {
      alert(err);
    });
  }

  componentDidUpdate() {
    Prism.highlightAll();
  }

  render() {
    if(this.state.isLoaded !== true) {
      return (
        <Spinner/>
      )
    }
    if(this.state.model === null) {
      return (
        <div className="container mx-auto px-10 mb-8">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-12">
            <div className="col-span-1 lg:col-span-8">
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
            </div>
            <div className="col-span-1 lg:col-span-4">
              <div className="relative lg:sticky top-8">
                  <Categories />
              </div>
            </div>
          </div>
        </div>
      )
    }

    return (
        <div className="container mx-auto px-10 mb-8">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-12">
            <div className="col-span-1 lg:col-span-8">
              <div className='bg-white shadow-lg rounded-lg lg:p-8 pb-12 mb-8'>
                <div className='relative overflow-hidden shadow-md mb-6'>
                  <img
                    src={this.state.model.image}
                    alt={this.state.model.title}
                    decoding='async'
                    loading='async'
                    fetchpriority='low'
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
                        {moment(this.state.model.created_at).format('YYYY年 M月 D日')}
                      </span>
                    </div>
                  </div>
                  <h1 className='mb-8 text-3xl font-semibold'>{this.state.model.title}</h1>
                  <div dangerouslySetInnerHTML={{__html: this.state.model.content}} />
                </div>
              </div>
            </div>
            <div className="col-span-1 lg:col-span-4">
              <div className="relative lg:sticky top-8">
                  <Categories />
              </div>
            </div>
          </div>
        </div>
    )
  }
}
export default withRouter(withTranslation()(PostDatailComponent));
