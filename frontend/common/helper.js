export const backendUrl = 'https://cal.liyangpu.com:8000';

export const request = function(url, method, data) {
  return uni.request({
    url: backendUrl + url,
    method: method,
    data: data,
    header: {
      Authorization: 'Token ' + uni.getStorageSync('token'),
      'Content-Type': 'application/x-www-form-urlencoded'
    },
  });
};

export const like = function(id) {
  return request('/dish/like/', 'POST', {
    dish_id: id,
    like: 1,
    dislike: 0,
    }).then(res => {
      console.log(res);
    });
};

export const dislike = function(id) {
  return request('/dish/like/', 'POST', {
    dish_id: id,
    like: 0,
    dislike: 1,
    }).then(res => {
      console.log(res);
    });
};

export default {
  backendUrl,
  request,
};
