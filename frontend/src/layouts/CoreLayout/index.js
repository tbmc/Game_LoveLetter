import React from 'react'
import Header from 'components/Header'

export default class CoreLayout extends React.Component {
  
  static propTypes = {
    children : React.PropTypes.element.isRequired
  }
  
  render() {
    const { children } = this.props
    return (
      <div className='container text-center'>
        <Header />
        <div className='core-layout__viewport'>
          {children}
        </div>
      </div>
    )
  }
}
