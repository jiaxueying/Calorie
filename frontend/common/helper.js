export const backendUrl = 'https://django-44k2-1813284-1311093683.ap-shanghai.run.tcloudbase.com:80';

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
