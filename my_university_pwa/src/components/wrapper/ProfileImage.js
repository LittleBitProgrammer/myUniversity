//IMPORT LIB
import React from 'react'
//BOOTSTRAP
import RoundedImage from '../bootstrap/RoundedImage';

// CREATE A COMPONENT
const ProfileImage = ({path,altText,sigle,inputText,isVisibleInput, className}) => {
    return (
        <div className={`profile-img ${className? className: null}`}>
            <div className='container-profile'>
                <RoundedImage path={path} alt={altText}/>
                <div className="profile-sigle">
                    {sigle}
                </div>
                {
                    inputText && isVisibleInput &&
                    <div className="file btn btn-lg btn-primary text-block">
                        {inputText}
                        <input type="file" name="file"/>
                    </div>
                }

            </div>
        </div>
    );
}

// SET DEFAULT PROPS
ProfileImage.defaultProps ={
    inputText: 'Change Photo',
    altText: 'Profile Image',
    sigle: 'AB',
    isVisibleInput: true
}

// EXPORT A COMPONENT
export default ProfileImage;