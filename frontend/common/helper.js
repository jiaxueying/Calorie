export const backendUrl = 'http://cal.hanlh.com:8000';

export const request = function(url, method, data) {
  return uni.request({
    url: backendUrl + url,
    method: method,
    data: data,
    header: {
      Authorization: 'Token ' + uni.getStorageSync('token'),
<<<<<<< HEAD
      'Content-Type': 'application/x-www-form-urlencoded'
=======
      'Content-Type': 'application/x-www-form-urlencoded',
      
>>>>>>> 5cad8c8f48b8c0cee644604e30755bdbeaf19bab
    },
  });
};

export default {
  backendUrl,
  request,
};
