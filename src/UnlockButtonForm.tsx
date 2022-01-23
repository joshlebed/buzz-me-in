import * as React from 'react';
import { useState } from 'react';
import lockFailed from './lock-failed.svg';
import lockUnlocked from './lock-unlocked.svg';
import lock from './lock.svg';
import {
  BodyP,
  ErrorP,
  LockIconImg,
  PasscodeInput,
  PasscodeInputContainer,
  Spinner,
  StyledForm,
  StyledLoadingOverlay,
  TitleP,
  UnlockButton,
  UnlockButtonContainer,
} from './SharedComponents';
import spinner from './spinner.svg';

interface renderLockIconProps {
  success: boolean;
  requested: boolean;
  loading: boolean;
}

const renderLockIcon: React.FunctionComponent<renderLockIconProps> = (props: renderLockIconProps) => {
  if (props.requested && !props.loading && !props.success) {
    return <LockIconImg src={lockFailed} alt="lock failed" />;
  }
  if (props.success) {
    return <LockIconImg src={lockUnlocked} alt="lock unlocked" />;
  }
  return <LockIconImg src={lock} alt="lock" color="red" />;
};

interface getInfoMessageProps {
  success: boolean;
  requested: boolean;
  loading: boolean;
  error: string;
}

const getInfoMessage: React.FunctionComponent<getInfoMessageProps> = (props: getInfoMessageProps) => {
  if (props.requested && !props.loading && !props.success) {
    return <ErrorP>{props.error}</ErrorP>;
  }
  if (props.success) {
    return <BodyP>welcome!</BodyP>;
  }
  if (props.loading) {
    return <BodyP>loading...</BodyP>;
  }
  return <BodyP>tap to unlock</BodyP>;
};

// const renderLockIcon: React.FunctionComponent<renderLockIconProps> = (props: renderLockIconProps) =>
// props.loading ? (
//   <LockIconImg src={lockUnlocked}  alt="lock" />
// ) : (
//   <LockIconImg src={lockFailed}  alt="lock" />
// );

const UnlockButtonForm: React.FunctionComponent = () => {
  const [requested, setRequested] = useState(false);
  const [loading, setLoading] = useState(false);
  const [passcode, setPasscode] = useState('');
  const [success, setSuccess] = useState(false);
  const [error, setError] = useState('');

  const sendUnlockRequest = (passcodeAttempt) => {
    setRequested(true);
    setLoading(true);
    setSuccess(false);
    setError('');
    fetch(`/api/unlock/${passcodeAttempt}`)
      .then((res) => res.json())
      .then((data) => {
        setSuccess(data.success);
        setError(data.message);
        setLoading(false);
      });
  };

  const handleChangeCode = (event) => {
    setPasscode(event.target.value);
  };

  const handleSubmit = (event) => {
    console.log(`current passcode: ${passcode}`);
    if (passcode) {
      sendUnlockRequest(passcode);
    } else {
      setSuccess(false);
    }
    event.preventDefault();
  };

  return (
    <StyledForm onSubmit={handleSubmit}>
      <TitleP>welcome to 166 orchard!</TitleP>
      <BodyP>enter your passcode:</BodyP>
      <PasscodeInputContainer>
        <PasscodeInput type="text" value={passcode} onChange={handleChangeCode} />
      </PasscodeInputContainer>
      <StyledLoadingOverlay
        spinner={<Spinner color="red" src={spinner} alt="loading spinner" />}
        active={loading}
        styles={{}}
        fadeSpeed={0}
        classNamePrefix="Loader_"
      >
        <UnlockButtonContainer>
          <UnlockButton type="submit" disabled={loading || !passcode}>
            {renderLockIcon({ success, requested, loading })}
          </UnlockButton>
        </UnlockButtonContainer>
      </StyledLoadingOverlay>
      {getInfoMessage({ success, requested, loading, error })}
    </StyledForm>
  );
};

export default UnlockButtonForm;
