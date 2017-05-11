import React from 'preact-compat'

class Power extends React.Component {

  render() {
    return (
      <li className={`power-${this.props.value}`}>
        <p>Power:</p>
        <svg viewBox='0 0 16 24'><path d='M15.649 9.165a.815.815 0 0 0-.778-.392l-3.724.379c-1.005.102-1.127-.018-1.057-.861l.596-7.025c.032-.368.08-1.107-.41-1.248-.42-.122-.86.42-1.07.723L.14 14.088a.81.81 0 0 0-.025.872.84.84 0 0 0 .779.391l3.859-.392c1.003-.102.994-.002.924.84l-.598 7.059c-.031.367.019.951.42 1.09.478.163.905-.34 1.059-.564 2.27-3.335 9.066-13.347 9.066-13.347a.811.811 0 0 0 .025-.873'></path></svg>
      </li>
    )
   }
 }

export default Power