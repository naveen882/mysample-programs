from mock import mock,Mock


mock = MagicMock(side_effect=[4, 5, 6])
print mock()
print mock()
print mock()
mock = Mock(side_effect=Exception('Boom!'))
print mock()
