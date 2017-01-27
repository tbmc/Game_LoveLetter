import React, { Component }     from 'react';
import { connect }              from 'react-redux';
import _                        from 'lodash';
import { Field, reduxForm }     from 'redux-form'


class Login extends Component {
  
  static propTypes = {};
  static defaultProps = {};
  
  componentWillMount() {
    this.submit = this.submit.bind(this)
    this.renderInputField = this.renderInputField.bind(this)
  }

  renderInputField(props) {
    const { meta: { error, touched }, label, type } = props;
    return (
      <div>
        <div>
          { label || "" }
          <input { ...props.input } type={type} />
        </div>
        <div style={{ color: "red", textAlign: "left" }}>
          { touched && error || ""}
        </div>
      </div>
    )
  }
  
  render() {
    const { handleSubmit } = this.props;
    return (
      <form onSubmit={handleSubmit(this.submit)}>
        
        <Field
          name="pseudo"
          component={this.renderInputField}
          type="text" label="Pseudo"
        />
        <Field
          name="password"
          component={this.renderInputField}
          type="password" label="Mot de passe"
        />
        
        <div>
          <button type="submit">
            Connexion
          </button>
        </div>
        
      </form>
    );
  }

  submit() {
    
  }
  
}


const validate = values => {
  let errors = {};
  
  if(!values.pseudo) {
    errors.pseudo = "Le pseudo ne doit pas être vide"
  }
  if(!values.password) {
    errors.password = "Le mot de passe ne doit pas être vide"
  }
  
  return errors;
}

// Decorate the form component
Login = reduxForm({
  validate,
  form: 'loginForm' // a unique name for this form
})(Login);


export default connect(
    ({}) => ({}),
    {}
)(Login);
