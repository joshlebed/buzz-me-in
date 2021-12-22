import * as React from 'react';
import { useState } from 'react';
import './App.css';
import lockFailed from './lock-failed.svg';
import lockUnlocked from './lock-unlocked.svg';
import lock from './lock.svg';

interface renderResultProps {
  success: boolean;
}

const renderResult: React.FunctionComponent<renderResultProps> = (props: renderResultProps) =>
  props.success ? (
    <img src={lockUnlocked} className="Lock-icon" alt="lock" />
  ) : (
    <img src={lockFailed} className="Lock-icon" alt="lock" />
  );

const App = () => {
  const [requested, setRequested] = useState(false);
  const [success, setSuccess] = useState();

  const handleClickLock = () => {
    fetch(`/api/unlock/${1}`)
      // .then((res) => {
      //   console.log(res);
      //   return res;
      // })
      .then((res) => res.json())
      .then((data) => {
        setSuccess(data.success);
        setRequested(true);
      });
  };

  return (
    <div className="App">
      <header className="App-header">
        {requested ? (
          renderResult({ success })
        ) : (
          <div onClick={handleClickLock} role="button" tabIndex={0} onKeyPress={handleClickLock}>
            <img src={lock} className="Lock-icon" alt="lock" />
          </div>
        )}
        <p>tap to unlock</p>
      </header>
    </div>
  );
};

export default App;
